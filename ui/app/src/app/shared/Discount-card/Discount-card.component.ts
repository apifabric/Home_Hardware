import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Discount-card.component.html',
  styleUrls: ['./Discount-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Discount-card]': 'true'
  }
})

export class DiscountCardComponent {


}