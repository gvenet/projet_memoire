import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  username: string = ''; 

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.register(this.username).subscribe(
      response => {
        this.authService.login(this.username).subscribe(
          response => {
            if (response.token) {
              this.router.navigate(['/home']);
            } else {
              console.error('Login error')
            }
          },
          error => {
            console.error('Login error:', error);
          }
        );
      },
      error => {
        console.error('Register error:', error);
      }
    );
  }
}
