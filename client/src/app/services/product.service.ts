import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from '../models/product.model';
import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = `${environment.apiUrl}/produits`;

  constructor(private http: HttpClient, private authService: AuthService) { }

  private createAuthHeaders(): HttpHeaders {
    const token = this.authService.getToken();
    return new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });
  }


  getProducts(): Observable<Product[]> {
    const headers = this.createAuthHeaders();
    return this.http.get<Product[]>(`${this.apiUrl}`, { headers });
  }

  getProduct(id: number): Observable<Product> {
    const headers = this.createAuthHeaders();
    return this.http.get<Product>(`${this.apiUrl}/${id}`, { headers });
  }

  isValidate(id: number): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.get<any>(`${this.apiUrl}/checkId/${id}`, { headers });
  }
}