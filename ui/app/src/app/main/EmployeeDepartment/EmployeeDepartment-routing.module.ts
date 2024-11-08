import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeDepartmentHomeComponent } from './home/EmployeeDepartment-home.component';
import { EmployeeDepartmentNewComponent } from './new/EmployeeDepartment-new.component';
import { EmployeeDepartmentDetailComponent } from './detail/EmployeeDepartment-detail.component';

const routes: Routes = [
  {path: '', component: EmployeeDepartmentHomeComponent},
  { path: 'new', component: EmployeeDepartmentNewComponent },
  { path: ':id', component: EmployeeDepartmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'EmployeeDepartment-detail-permissions'
      }
    }
  }
];

export const EMPLOYEEDEPARTMENT_MODULE_DECLARATIONS = [
    EmployeeDepartmentHomeComponent,
    EmployeeDepartmentNewComponent,
    EmployeeDepartmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeeDepartmentRoutingModule { }