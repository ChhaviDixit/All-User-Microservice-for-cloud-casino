import graphene
from resolvers import resolve_players
from enum import Enum

class Players(graphene.ObjectType):
    username= graphene.String()

class Query(graphene.ObjectType):
    players = graphene.List(Players)

    def resolve_players(self, info):
        return resolve_players()

schema = graphene.Schema(query=Query)
