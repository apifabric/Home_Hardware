import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Return-card.component.html',
  styleUrls: ['./Return-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Return-card]': 'true'
  }
})

export class ReturnCardComponent {


}