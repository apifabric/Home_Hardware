import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DISCOUNT_MODULE_DECLARATIONS, DiscountRoutingModule} from  './Discount-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DiscountRoutingModule
  ],
  declarations: DISCOUNT_MODULE_DECLARATIONS,
  exports: DISCOUNT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DiscountModule { }