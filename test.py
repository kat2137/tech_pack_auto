from output_structure import analyze_drawing

result = analyze_drawing("assets/images/sample.png")
print(result.stitch_table)
print(result.bom)
print(result.fabrics)