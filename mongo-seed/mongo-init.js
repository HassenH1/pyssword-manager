db.createCollection("collection");
db.collection.insert([
  {
    site: "Facebook",
    username: "jsmith@gmail.com",
    password: "somepassword",
  },
  {
    site: "Google",
    username: "jford@gmail.com",
    password: "password some",
  },
]);
