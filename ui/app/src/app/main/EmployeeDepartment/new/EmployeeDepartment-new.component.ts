import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'EmployeeDepartment-new',
  templateUrl: './EmployeeDepartment-new.component.html',
  styleUrls: ['./EmployeeDepartment-new.component.scss']
})
export class EmployeeDepartmentNewComponent {
  @ViewChild("EmployeeDepartmentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}