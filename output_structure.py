import anthropic
import base64
from pydantic import BaseModel
from typing import List, Optional
from models import stitch_type, seam_type


client = anthropic.Anthropic ()

class StitchRow(BaseModel):
    stitch_type: str
    seam_type: str
    area: str
    stitch_image: str
    thread_type: int
    thread_color: str

class BOMitem(BaseModel):
    item_name: str
    item_color: str
    item_image: str
    quantity: int
    unit: str

class Fabric(BaseModel):
    fabric_name: str
    fabric_color: str
    fabric_image: str

CSTITCHES = "\n".join(f"-{s}" for s in stitch_type)
CSEAMS = "\n".join(f"-{s}" for s in seam_type)    

#if str.lower(thread_color) =="dtm":
#    thread_color = str.lower(main_fabric_color)

#if fabric > 1:
#    fabric_list.append(fabric_name: str, fabric_color: str, fabric_image: str)

#if len(fabric_list) >1:   

class TechPackAnalysis(BaseModel):
    stitch_table: List[StitchRow]
    bom: List[BOMitem]
    fabrics: List[Fabric]

SYSTEM_PROMPT = f"""You are a garment technical designer analyzing a tech pack. Your task is to extract structured information about the stitching and materials used in the garment on this drawing.

The first page that has a color drawing of the garment should be used to extract fabric color information. Fabric type should be mentioned there as well.

The line drawings, usually page 2 and 3, should be used to analyse stitch and seam types. 
You must map every stitch you identify to one of these types, deciding based on fabric quality and seam appearance:
{CSTITCHES}

Common mappings include:
- topstich, edgestitch, 'bagged out' seams → lockstitch
- raw edges, knits → overlock
- hems → blind stitch or babylock and lockstitch if fabric is delicate
- flat seams on athletic wear and t-shirts → flatlock
- denim seams with visible topstitching → twin-needle stitch
- bra underwires → twin-needle stitch
- elastics on lingerie → zigzag or three step zigzag or coverstitch
- ends of straps on lingerie → bartack
- denim belt loops → bartack
- two-line topstitch - twin-needle stitch

You must also map every seam to one of these types:{CSEAMS}

Always use the canonical name in stitch_type and seam_type lists. If you cannot confidently identify a stitch or seam, leave it blank. Do not invent new types.
Use description-style fields to record the specific application name."""

def analyze_drawing(file_path: str) -> TechPackAnalysis:
    ext = file_path.lower().rsplit(".",1) [-1]
    media_type = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png", 
        "webp": "image/webp",
    }.get(ext, "image/jpeg")

    with open(file_path, "rb") as f:
    file_data = base64.standard_b64encode(f.read()).decode("utf-8")

    response = client.messages.parse(
        model="claude-opus-4-6",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": file_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Analyse this tech pack drawing. Identify all stitch types, seam types, fabrics, and build a full bill of materials.",
                },
            ],
        }],
       output_format=TechPackAnalysis,
    )
    return response.parsed_output