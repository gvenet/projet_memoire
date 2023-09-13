import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  apiUrl: string = 'http://localhost:5001';

  constructor(
    private http: HttpClient,
    private cookieService: CookieService) { }

  login(username: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login`, { username }).pipe(
      map((response: { token: string; userId: number; }) => {
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

}
