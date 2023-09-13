import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { CardComponent } from './components/card/card.component';
import { DetailComponent } from './components/detail/detail.component';

import { RouterModule } from '@angular/router';
import { CartComponent } from './components/cart/cart.component';
import { LoginComponent } from './components/login/login.component';
import { FormsModule } from '@angular/forms';
import { NavbarComponent } from './components/navbar/navbar.component';
import { RegisterComponent } from './components/register/register.component';
import { QuantityEditModalComponent } from './components/quantity-edit-modal/quantity-edit-modal.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CardComponent,
    DetailComponent,
    CartComponent,
    LoginComponent,
    NavbarComponent,
    RegisterComponent,
    QuantityEditModalComponent,
    
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot([]),
    FormsModule,
    NgbModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
