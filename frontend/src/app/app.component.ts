import { Component } from '@angular/core';
import {UserService} from './service/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  isLoggedIn = false;

  constructor(private userService: UserService) {
    this.userService.isLoggedIn.subscribe((isLoggedIn) => {this.isLoggedIn = isLoggedIn;
    });
  }
}
