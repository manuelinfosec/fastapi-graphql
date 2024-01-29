import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from colorama import init

from core import Mutation, Query

# initilize terminal color support
init()

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def ping():
    return {"ping": "pong"}
