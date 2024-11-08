import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DiscountHomeComponent } from './home/Discount-home.component';
import { DiscountNewComponent } from './new/Discount-new.component';
import { DiscountDetailComponent } from './detail/Discount-detail.component';

const routes: Routes = [
  {path: '', component: DiscountHomeComponent},
  { path: 'new', component: DiscountNewComponent },
  { path: ':id', component: DiscountDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Discount-detail-permissions'
      }
    }
  }
];

export const DISCOUNT_MODULE_DECLARATIONS = [
    DiscountHomeComponent,
    DiscountNewComponent,
    DiscountDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DiscountRoutingModule { }