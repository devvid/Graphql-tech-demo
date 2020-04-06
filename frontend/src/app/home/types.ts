export type Author = {
  id: number;
  name: string;
  email: string;
}

export type ViewHistory = {
  id: number,
  ipAddress: string,
  created: string
}
  
export type Post = {
  id: number;
  title: string;
  body: string;
  author: Author
  history: {
    edges: [{
      node: ViewHistory
    }]
  }
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
