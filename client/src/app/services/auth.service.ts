import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import { environment } from 'src/environments/environment';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  apiUrl: string = environment.apiUrl;

  constructor(
    private http: HttpClient,
    private cookieService: CookieService) {
    console.log('environment : ' + environment);
    console.log('environment.production : ' + environment.production);
    console.log('environment.production : ' + this.apiUrl);
  }

  private createAuthHeaders(): HttpHeaders {
    const token = this.getToken();
    return new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });


  }

  login(username: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login`, { username }).pipe(
      map((response: { token: string; }) => {
        if (response && response.token) {
          this.cookieService.set('authToken', response.token, 30);
        }
        return response;
      })
    );
  }

  register(username: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/register`, { username });
  }

  isAuthenticated(): boolean {
    return !!this.cookieService.get('authToken')
  }

  logout(): void {
    this.cookieService.delete('authToken');
  }

  getToken(): string {
    return this.cookieService.get('authToken');
  }

  isAdmin(): Observable<any> {
    const headers = this.createAuthHeaders();
    return this.http.get(`${this.apiUrl}/isAdmin`, { headers });
  }

}
