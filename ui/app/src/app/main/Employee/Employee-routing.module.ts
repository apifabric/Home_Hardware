import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeHomeComponent } from './home/Employee-home.component';
import { EmployeeNewComponent } from './new/Employee-new.component';
import { EmployeeDetailComponent } from './detail/Employee-detail.component';

const routes: Routes = [
  {path: '', component: EmployeeHomeComponent},
  { path: 'new', component: EmployeeNewComponent },
  { path: ':id', component: EmployeeDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Employee-detail-permissions'
      }
    }
  },{
    path: ':manager_id/Department', loadChildren: () => import('../Department/Department.module').then(m => m.DepartmentModule),
    data: {
        oPermission: {
            permissionId: 'Department-detail-permissions'
        }
    }
},{
    path: ':employee_id/EmployeeDepartment', loadChildren: () => import('../EmployeeDepartment/EmployeeDepartment.module').then(m => m.EmployeeDepartmentModule),
    data: {
        oPermission: {
            permissionId: 'EmployeeDepartment-detail-permissions'
        }
    }
}
];

export const EMPLOYEE_MODULE_DECLARATIONS = [
    EmployeeHomeComponent,
    EmployeeNewComponent,
    EmployeeDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EmployeeRoutingModule { }