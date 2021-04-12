from server.database import get_collection

colors_collection = get_collection('dreamWebSite', 'colors')

# Helpers

def color_helper(color) -> dict:
    return {
        "id": str(color["_id"]),
        "color_usage": color["color_usage"],
        "color_type": color["color_type"],
        "color_hex": color["color_hex"]
    }
    
# CRUD

# Get all colors
async def retrieve_colors():
    colors = []
    async for color in colors_collection.find():
        colors.append(color_helper(color))
    return colors

# Register new option color
async def add_color(color_data: dict) -> dict:
    color = await colors_collection.insert_one(color_data)
    new_color = await colors_collection.find_one({"_id": color.inserted_id})
    return color_helper(new_color)