from fastapi import FastAPI

app = FastAPI()

#http://localhost:8000/test
#get api...
@app.get("/test/")
async def test():
    return "Hello"

@app.get("/users/")
async def getAllUsers():
    return {"message":"Users fatched successfully!!","users":["ram","shyam","seeta","geeta"]}


@app.get("/user/{userId}")
async def getUserById(userId:str):
    return {"messafe":f"user found with id {userId}"}
    #return  {"message":"user found with id "+userId}
     