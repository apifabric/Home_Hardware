import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Discount-new',
  templateUrl: './Discount-new.component.html',
  styleUrls: ['./Discount-new.component.scss']
})
export class DiscountNewComponent {
  @ViewChild("DiscountForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}