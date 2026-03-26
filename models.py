
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class StitchStep:
    stitch_type: Optional[str] = None
    seam_type: Optional[str] = None
    area: Optional[str] = None


stitch_type = [
    "lockstitch",
    "three - thread overlock",
    "four - thread overlock",
    "five - thread overlock",
    "coverstitch",
    "flatlock",
    "single thread chainstitch",
    "twin-needle stitch",
    "blind stitch",
    "zigzag",
    "three step zigzag",
    "bartack",
    "hand tuck",
    "babylock",
    "cross stitch",
    "round buttonhole",
    "straight buttonhole",
    "keyhole buttonhole",
]

seam_type = [
    "plain seam",
    "French seam",
    "flat-felled seam",
    "bound seam",
    "piped seam"
]

stitch_image = [
    "lockstitch.png",
    "3threadoverlock.png",
    "4threadoverlock.png",
    "5threadoverlock.png",
    "coverstitch.png",
    "flatlock.png",
    "chainstitch.png",
    "twinneedle.png",
    "blindstitch.png",
    "zigzag.png",
    "3stepzigzag.png",
    "bartack.png",
    "handtuck.png",
    "babylock.png",
    "crossstitch.png",
    "roundbuttonhole.png",
    "straightbuttonhole.png",
    "keyholebuttonhole.png",
    ""
]

def stitch_image(stitch_type):
     for x in stitch_type:
        if str(x) in stitch_image and stitch_image.index(str(x)) == stitch_type.index(str(x)):
         print(x + stitch_image[stitch_type.index(str(x))])
        if str(x) not in stitch_image:
            print(x + "no image")