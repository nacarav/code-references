import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; // module to perform http request
import { NavController } from '@ionic/angular';
import { HttpResponse } from '../models/http-response'; // class which specifies what our response from the api should look like

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private token: string; // declare our token variable that will hold our token while using the app

  constructor(private http: HttpClient, private navController: NavController) { }

  login(email, password) {
    this.http.post('http://localhost:5000/api/auth/login', {email: email, password: password}).subscribe((response: HttpResponse) => {
      if (response.success) { // successful http request, same format as HttpResponse model / class
        this.token = response.data; // set our token to the data in the response object
        this.navController.navigateForward('users'); // navigate to the users page
      }
      else {
        alert(response.message); // display an alert if response has an error 
      }
      console.log(response);
    });
  }

  register(user) {
    this.http.post('http://localhost:5000/api/auth/register', user).subscribe((response: HttpResponse) => {
      if (response.success) { // successful http request, same format as HttpResponse model / class
        this.token = response.data; // set our token to the data in the response object
        this.navController.navigateForward('users'); // navigate to the users page
      }
      else {
        alert(response.message); // display an alert if response has an error 
      }
      console.log(response);
    });
  }

  getToken(): string { // get our token from another service or component in our app
    return this.token
  }

  setTokenToEmpty() {
    this.token = ""; // reset the token to an empty string
  }

}
