import { Injectable }     from '@angular/core';
import { Http } from '@angular/http';
import { UserData }           from './userData';
import { Observable }     from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class GreetService {
  constructor (private http: Http) {}

  private baseUrl = 'http://127.0.0.1:5000/';  // URL to web API

  getGreetings (name: string): Observable<UserData>{
    return this.http.get(this.baseUrl + name).map(res => <UserData> res.json());
  }

}