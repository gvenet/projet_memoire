import { Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-quantity-edit-modal',
  templateUrl: './quantity-edit-modal.component.html',
})
export class QuantityEditModalComponent {
  @Input() quantity!: number;
  @Input() productId!: number;
  quantityForm: FormGroup;

  constructor(
    public activeModal: NgbActiveModal,
    private formBuilder: FormBuilder) {
    this.quantityForm = this.formBuilder.group({
      newQuantity: [this.quantity, [Validators.required, Validators.min(1)]],
    });
  }

  save(): void {
    if (this.quantityForm.valid) {
      const newQuantity = parseInt(this.quantityForm.value.newQuantity, 10);

      
      if (!isNaN(newQuantity) && newQuantity >= 1) { 
        this.activeModal.close({ saved: 'saved', productId: this.productId, quantity: newQuantity});
      } else {
        console.error('La nouvelle quantité n\'est pas valide.');
      }
    }
  }
}
