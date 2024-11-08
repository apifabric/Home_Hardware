import { MenuRootItem } from 'ontimize-web-ngx';

import { CategoryCardComponent } from './Category-card/Category-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DepartmentCardComponent } from './Department-card/Department-card.component';

import { DiscountCardComponent } from './Discount-card/Discount-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { EmployeeDepartmentCardComponent } from './EmployeeDepartment-card/EmployeeDepartment-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ReturnCardComponent } from './Return-card/Return-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Category', name: 'CATEGORY', icon: 'view_list', route: '/main/Category' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Department', name: 'DEPARTMENT', icon: 'view_list', route: '/main/Department' }
    
        ,{ id: 'Discount', name: 'DISCOUNT', icon: 'view_list', route: '/main/Discount' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'EmployeeDepartment', name: 'EMPLOYEEDEPARTMENT', icon: 'view_list', route: '/main/EmployeeDepartment' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Return', name: 'RETURN', icon: 'view_list', route: '/main/Return' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CategoryCardComponent

    ,CustomerCardComponent

    ,DepartmentCardComponent

    ,DiscountCardComponent

    ,EmployeeCardComponent

    ,EmployeeDepartmentCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,ProductCardComponent

    ,ReturnCardComponent

    ,SupplierCardComponent

];