import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { ProductService } from '../services/product.service';

@Injectable({
  providedIn: 'root',
})
export class ProductGuard implements CanActivate {
  constructor(private router: Router, private productService: ProductService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> {
    const id = route.paramMap.get('id');
    if (!id || isNaN(parseInt(id))) {
      this.router.navigate(['/home']);
      return of(false);
    }

    return this.productService.getProduct(parseInt(id)).pipe(
      switchMap((response) => {
        return of(true);
      }),
      catchError((error) => {
        console.error(error)
        this.router.navigate(['/home']);
        return of(false);
      })
    );

  }
}
