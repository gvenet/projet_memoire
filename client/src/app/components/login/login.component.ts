// login.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = ''; // Propriété liée au champ d'entrée
  password: string = ''; // Ajoutez ce champ si vous avez besoin du mot de passe

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    // Appelez la méthode de service d'authentification pour vérifier les informations d'identification
    this.authService.login(this.username).subscribe(
      response => {
        // Gérez la réponse réussie ici (par exemple, stockez le jeton d'authentification)
        if (response.token) {
          // Redirigez l'utilisateur vers la page d'accueil ou une autre page
          this.router.navigate(['/home']);
        } else {
          console.error('token error')
        }
      },
      error => {
        // Gérez les erreurs ici (par exemple, affichez un message d'erreur)
        console.error('Login error:', error);
      }
    );
  }
}
