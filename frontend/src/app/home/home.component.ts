import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import gql from 'graphql-tag';

import { Post, Node, Query } from './types';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})
export class HomeComponent implements OnInit {

  posts: Observable<Node[]>;
  constructor(private apollo: Apollo) {}

  ngOnInit(): void {
    this.posts = this.apollo.watchQuery<Query>({
      query: gql`
        { allPosts{
          edges{
            node{
              id
              title
              body
              author {
                id
                name
                email
              }
            }
          }
        }
      }
      `,
    })
      .valueChanges
      .pipe(
        map(result => result.data.allPosts.edges)
      );
    console.log(this.posts)
  }

  
}
