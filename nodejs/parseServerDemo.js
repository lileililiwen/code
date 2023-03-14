const express = require('express');
const ParseServer = require('parse-server').ParseServer;
const app = express();

const api = new ParseServer({
    databaseURI: 'mongodb://localhost:27017/dev',
    appId: 'myAppId',
    masterKey: 'myMasterKey',
    serverURL: 'http://localhost:1337/parse'
});

app.use('/parse', api);

app.listen(1337, function() {
    console.log('parse-server-example running on port 1337.');
});

// Create a new instance of the Parse SDK
const Parse = require('parse/node');
Parse.initialize('myAppId', '', 'myMasterKey');
Parse.serverURL = 'http://localhost:1337/parse';

// Define a new class called "Post"
const Post = Parse.Object.extend("Post");

// Create a new post
async function createPost(title, content) {
    const post = new Post();
    post.set("title", title);
    post.set("content", content);
    try {
        await post.save();
        console.log(`New object created with objectId: ${post.id}`);
        return post;
    } catch (error) {
        console.error(`Failed to create new object, with error code: ${error.message}`);
        return null;
    }
}

// Get all posts with pagination
async function getPosts(page=1, perPage=5) {
    const query = new Parse.Query(Post);
    query.skip((page - 1) * perPage);
    query.limit(perPage);
    try {
        const results = await query.find();
        console.log(`Successfully retrieved ${results.length} posts.`);
        return results;
    } catch (error) {
        console.error(`Error while fetching posts: ${error.message}`);
        return [];
    }
}

// Update a post by id
async function updatePost(id, title, content) {
   const query=new Parse.Query(Post);
   try{
      const post=await query.get(id);
      post.set("title",title);
      post.set("content",content);
      await post.save();
      console.log(`Object updated with objectId:${post.id}`);
      return true;
   }catch(error){
       console.error(`Failed to update object with error code:${error.message}`);
       return false;
   }
}

// Delete a post by id
async function deletePost(id){
   const query=new Parse.Query(Post);
   try{
       const post=await query.get(id);
       await post.destroy();
       console.log(`Object deleted with objectId:${post.id}`);
       return true;
   }catch(error){
       console.error(`Failed to delete object with error code:${error.message}`);
       return false;
   }
}