import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { CartItemCountService } from 'src/app/services/cart-item-count.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  cartItemCount!: number;

  constructor(private authService: AuthService, private cartItemCountService: CartItemCountService) { }

  ngOnInit(): void {
    this.cartItemCountService.getCartItemCount().subscribe(count => {
      this.cartItemCount = count;
    });
  }

  logout(): void {
    this.authService.logout();
  }

  isLoggedIn(): boolean {
    return this.authService.isAuthenticated();
  }
}
