import graphene
from resolvers.queries import Query
from resolvers.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)