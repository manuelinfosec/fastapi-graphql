## Why GraphQL (over REST)?

REST is the de-facto standard for building web APIs. With REST, there are mulitple endpionts for each CRUD operation: GET, POST, PUT, DELETE. Data is gathered by accessing a number of endpoints.

For example, if you wanted to get a particular user's profile info along with their posts and relevant comments, you would need to call four different endpoints:

`/users/<id>` returns the initial user data
`/users/<id>/posts` returns all posts for a given user
`/users/<post_id>/comments `returns a list of comments per post
`/users/<id>/comments` returns a list of comments per user

This can result in request overfetching since you'll probably have to get much more data than you need.

GraphQL, meanwhile, is a query language for retrieving data from an API. Instead of having multiple endpoints, GraphQL is structured around a single endpoint whose return value is dependent on what the client wants instead of what the endpoint returns.

In GraphQL, you would structure a query like so to obtain a user's profile, posts, and comments:

```
query {
  User(userId: 2){
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```

All the data is gotten in just one request with no overfetching since the exact resource was specified. 

> FastAPI supports GraphQL via [Starlette](https://www.starlette.io/graphql) and [Graphene](https://graphene-python.org/). Starlette executes GraphQL queries in a seperate thread by default when async request handlers are no used


## Why Masonite ORM?

Masonite ORM is known to be clean, easy-to-use, object relational mapping library built for the Masonite web framework. It resembles other popular Active Record implementation, like Django's ORM, Laravel's Eloquent, AdonisJS' Lucid, and active Record in Ruby on Rails, with support for MySQL, Postgres and SQLite.

With the emphasis on convention over configuration, it's easy to create models since you don't have to expllicitly define every single aspect. Relationships are a breeze and very easy to handle as well.

## Starting the Server
1. Install dependencies from `requirements.txt`:
```
pip install -r requirements.txt
```

2. To start the server, open your terminal, navigate to the project directory, and enter the following command:
```
uvicorn main:app
```

3. Access the beautiful docs at http://localhost:8000/docs or http://localhost:8000/redocs
