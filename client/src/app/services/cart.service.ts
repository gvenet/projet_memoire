import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  apiUrl: string = environment.apiUrl;

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) { }

  private createAuthHeaders(): HttpHeaders {
    const token = this.authService.getToken();
    return new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });
  }

  getCartItemCount(): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.get<any>(`${this.apiUrl}/cart/item-count`, { headers });
  }

  getCart(): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.get(`${this.apiUrl}/cart/products`, { headers });
  }

  getCartItem(productId: number): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.get(`${this.apiUrl}/cart/product/${productId}`, { headers });
  }

  updateProductQuantity(productId: number, quantity: number): Observable<any> {
    const headers = this.createAuthHeaders();
    const data = { productId, quantity };
    return this.http.put(`${this.apiUrl}/cart/update-product`, data, { headers });
  }

  addToCart(productId: number, quantity: number): Observable<any> {
    const headers = this.createAuthHeaders();
    const data = { productId, quantity };
    return this.http.post(`${this.apiUrl}/cart/add-product`, data, { headers });
  }

  removeFromCart(productId: number): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.delete(`${this.apiUrl}/cart/delete-product/${productId}`, { headers });
  }
}
