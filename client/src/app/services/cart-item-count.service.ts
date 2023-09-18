import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { CartService } from './cart.service';

@Injectable({
  providedIn: 'root'
})
export class CartItemCountService {
  private cartItemCountSubject = new BehaviorSubject<number>(0);

  constructor(private cartService: CartService) {
    this.updateCartItemCount(); 
  }

  private updateCartItemCount(): void {
    this.cartService.getCartItemCount().subscribe(
      (count: any) => {
        this.cartItemCountSubject.next(count.count);
      },
      (error) => {
        console.error('Erreur lors de la récupération du nombre d\'articles dans le panier :', error);
      }
    );
  }

  getCartItemCount(): Observable<number> {
    this.updateCartItemCount();
    // Vous pouvez maintenant renvoyer directement l'observable BehaviorSubject
    return this.cartItemCountSubject.asObservable();
  }
}