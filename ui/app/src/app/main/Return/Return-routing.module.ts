import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReturnHomeComponent } from './home/Return-home.component';
import { ReturnNewComponent } from './new/Return-new.component';
import { ReturnDetailComponent } from './detail/Return-detail.component';

const routes: Routes = [
  {path: '', component: ReturnHomeComponent},
  { path: 'new', component: ReturnNewComponent },
  { path: ':id', component: ReturnDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Return-detail-permissions'
      }
    }
  }
];

export const RETURN_MODULE_DECLARATIONS = [
    ReturnHomeComponent,
    ReturnNewComponent,
    ReturnDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReturnRoutingModule { }