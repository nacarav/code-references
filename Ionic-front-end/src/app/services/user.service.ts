import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'; // module to perform http request and set http headers
import { AuthenticationService } from './auth.service'; // authentication service which holds our token
import { User } from '../models/user'; // user model
import { NavController } from '@ionic/angular';
import { HttpResponse } from '../models/http-response'; // class which specifies what our response from the api should look like

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private userToUpdate: User; // user the our update user page will update
  private callBack: Function; // callback function (deleteUser) that we can call from any page which imports this service 

  httpOptions: { // declare our http options - used to create our http headers which will store our token
    headers: HttpHeaders
  };

  constructor(private http: HttpClient, private authenticationService: AuthenticationService, private navController: NavController) {
    
  }

  getUsers(): any { 
    this.httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + this.authenticationService.getToken() // get our token from the authentication service and add it the http headers
      })
    };
    return this.http.get('http://localhost:5000/api/users', this.httpOptions); // this returns an observable object which allows which ever function that calls get users to receive the http request for get users 
  }

  setUserToUpdate(user: User) {
    this.userToUpdate = user; // set the user that we should update in our update user page
  }

  getUserToUpdate(): User {
    return this.userToUpdate; // get the user that we should update in our update user page
  }

  setCallBack(callback: Function) {
    this.callBack = callback; // set our callback function (deleteUser)
  }

  invokeCallBack(user) {
    this.callBack(user); // call our callback function (deleteUser) from another page or service
  }

  deleteUser(user: User) {
    this.httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + this.authenticationService.getToken() // get our token from the authentication service and add it the http headers
      })
    };
    this.http.post('http://localhost:5000/api/users/delete/' + user.id, {userId: user.id}, this.httpOptions).subscribe((response: HttpResponse) => {
      if (response.success) { // successful http request, same format as HttpResponse model / class
        this.navController.navigateForward('users'); // navigate to the users page
      }
      else {
        alert(response.message); // display an alert if response has an error 
      }
      console.log(response);
    });
  }

  updateUser(user: User) {
    this.httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + this.authenticationService.getToken() // get our token from the authentication service and add it the http headers
      })
    };
    this.http.post('http://localhost:5000/api/users/update', user ,this.httpOptions).subscribe((response: HttpResponse) => {
      if (response.success) { // successful http request, same format as HttpResponse model / class
        this.navController.navigateForward('users'); // navigate to the users page
      }
      else {
        alert(response.message); // display an alert if response has an error 
      }
      console.log(response);
    });
  }

}
