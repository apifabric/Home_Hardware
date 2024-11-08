import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './EmployeeDepartment-card.component.html',
  styleUrls: ['./EmployeeDepartment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.EmployeeDepartment-card]': 'true'
  }
})

export class EmployeeDepartmentCardComponent {


}