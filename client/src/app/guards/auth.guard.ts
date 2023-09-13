import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) {}

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): boolean {
    if (this.authService.isAuthenticated()) {
      return true; // L'utilisateur est authentifié, autoriser l'accès
    } else {
      // L'utilisateur n'est pas authentifié, redirigez-le vers la page de connexion
      this.router.navigate(['/login']);
      return false;
    }
  }
}
