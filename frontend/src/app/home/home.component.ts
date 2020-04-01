import { Component, OnInit, OnDestroy } from '@angular/core';
import { Apollo } from 'apollo-angular';
import { Observable, Subscription } from 'rxjs';
import { map } from 'rxjs/operators';

import gql from 'graphql-tag';

import { Post, Node, Query } from './types';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})
export class HomeComponent implements OnInit, OnDestroy {

  posts: Node[];

  subscriptions: Subscription[] = [];
  
  constructor(private apollo: Apollo) {}

  ngOnInit(): void {
    this.subscriptions.push(this.apollo.watchQuery<Query>({
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
      .subscribe(({ data, loading }) => {
        this.posts = data.allPosts.edges;
      })
    )
  }

  ngOnDestroy() {
    this.subscriptions.forEach(e => {
      e.unsubscribe();
    })
  }

  
}
