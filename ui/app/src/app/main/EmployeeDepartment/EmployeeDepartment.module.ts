import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {EMPLOYEEDEPARTMENT_MODULE_DECLARATIONS, EmployeeDepartmentRoutingModule} from  './EmployeeDepartment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    EmployeeDepartmentRoutingModule
  ],
  declarations: EMPLOYEEDEPARTMENT_MODULE_DECLARATIONS,
  exports: EMPLOYEEDEPARTMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class EmployeeDepartmentModule { }