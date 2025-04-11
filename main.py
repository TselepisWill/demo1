from fastapi import FastAPI

app = FastAPI()

food_list = ["Apple", "Banana", "Chicken", "Beef"]

@app.get("/foods")
async def get_strings():
    return {"foods": food_list}

@app.post("/foods")
async def add_string(name: str = ""):
    food_list.append(name)
    return {"foods": food_list}

@app.delete("/foods")
async def delete_string(index: int = 0):
    food_list.pop(index)
    return {"foods": food_list}