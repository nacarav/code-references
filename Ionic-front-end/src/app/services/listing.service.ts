import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'; // module to perform http request and set http headers
import { AuthenticationService } from './auth.service'; // authentication service which holds our token

@Injectable({
  providedIn: 'root'
})
export class ListingService {

  httpOptions: { // declare our http options - used to create our http headers which will store our token
    headers: HttpHeaders
  };

  constructor(private http: HttpClient, private authenticationService: AuthenticationService) {
  }

  getListings(): any {
    this.httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + this.authenticationService.getToken() // get our token from the authentication service and add it the http headers
      })
    };
    return this.http.get('http://localhost:5000/api/listings', this.httpOptions); // this returns an observable object which allows which ever function that calls get users to receive the http request for get listings 
  }

}
