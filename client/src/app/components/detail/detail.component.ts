import { Component,  OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CartItemCountService } from 'src/app/services/cart-item-count.service';
import { CartService } from 'src/app/services/cart.service';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {
  

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private cartService: CartService,
    private cartItemCountService: CartItemCountService) { }

  ngOnInit(): void {
    // Récupérer l'identifiant du produit depuis l'URL
    this.route.params.subscribe(params => {
      // Utilisez l'identifiant pour charger les détails du produit depuis votre service ou votre API
      this.productService.getProduct(params['id']).subscribe(product => this.product = product);
    });
  }

  quantite: number = 1;
  product: any;
  addToCart(): void {
    if (this.product) {
      this.cartService.getCartItem(this.product.id).subscribe(
        (cartItem) => {
          const newQuantity = cartItem.quantity + this.quantite;
          this.cartService.updateProductQuantity(cartItem.id, newQuantity).subscribe(() => {
            // Mettez à jour le service avec le nouveau nombre d'articles dans le panier
            this.cartItemCountService.getCartItemCount();
          });
        },
        () => {
          this.cartService.addToCart(this.product.id, this.quantite).subscribe(() => {
            // Mettez à jour le service avec le nouveau nombre d'articles dans le panier
            this.cartItemCountService.getCartItemCount();
          });
        }
      );
    }
  }
}

