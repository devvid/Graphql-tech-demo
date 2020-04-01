export type Author = {
    id: number;
    name: string;
    email: string;
  }
  
  export type Post = {
    id: number;
    title: string;
    body: string;
    author: Author
  }

  export type Node = {
    node: Post;
  }
  
  export type Query = {
    allPosts: {
      edges: Node[]
    }
  }
  
  export type Mutation = {
    upvotePost: Post;
  }
  