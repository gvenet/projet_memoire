import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product.model';
import { CartItemCountService } from 'src/app/services/cart-item-count.service';
import { CartService } from 'src/app/services/cart.service';
import { QuantityEditModalComponent } from '../quantity-edit-modal/quantity-edit-modal.component';


@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  cartProducts: any[] = []; // Tableau pour stocker les produits du panier
  quantity: number = 0;
  previousQuantity: number = 0;
  
  constructor(
    private cartService: CartService,
    private cartItemCountService: CartItemCountService,
    private modalService: NgbModal) { }

  ngOnInit(): void {
    // Appelez la méthode getCart de votre cartService pour récupérer le panier
    this.get_products();
  }

  get_products(): void {
    this.cartService.getCart().subscribe(
      (data: any[]) => {
        this.cartProducts = data;
      },
      (error) => {
        console.error('Erreur lors de la récupération du panier :', error);
      }
    );
  }

  removeItem(product: Product): void{
    this.cartService.removeFromCart(product.id).subscribe(() => {
      this.get_products();
      this.cartItemCountService.getCartItemCount();
    });
  }

  openQuantityEditModal(productId: number, quantity: number): void {
    const modalRef = this.modalService.open(QuantityEditModalComponent);
    
    modalRef.componentInstance.quantity = quantity;
    modalRef.componentInstance.productId = productId;

    modalRef.result.then((result) => {
      if (result.saved === 'saved') {
        this.cartService.updateProductQuantity(result.productId, result.quantity).subscribe(
          () => {
            this.get_products();
            this.cartItemCountService.getCartItemCount();
          }
          );
      }
    });
  }

}
