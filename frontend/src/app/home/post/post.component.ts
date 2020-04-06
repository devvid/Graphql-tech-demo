import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Apollo } from 'apollo-angular';
import { Observable, Subscription } from 'rxjs';
import { map } from 'rxjs/operators';
import { Post, Node } from '../types';

import gql from 'graphql-tag';

type Query = {
  post: Post;
}

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.sass']
})
export class PostComponent implements OnInit, OnDestroy  {

  id: string;
  post: Post;

  subscriptions: Subscription[] = [];

  constructor(
    private route: ActivatedRoute,
    private apollo: Apollo
  ) { 
    
  }

  ngOnInit(): void {
    this.subscriptions.push(this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
      this.query()
    }))
  }

  ngOnDestroy() {
    this.subscriptions.forEach(e => {
      e.unsubscribe();
    })
  }


  query() {
    this.subscriptions.push(this.apollo.watchQuery<Query>({
      query: gql`
      {
        post(id:"${this.id}"){
          id
          title
          body
          author {
            id
            name
          }
          history{
            edges{
              node{
                id
                ipAddress
              }
            }
          }
        }
      }
      `,
    })
    .valueChanges
    .subscribe(({ data, loading }) => {
      this.post = data.post;
    })
  )
  }
}
