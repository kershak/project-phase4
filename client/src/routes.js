import App from "./App";
import Home from "./pages/Home";
import About from "./pages/About";
import ContactPage from "./pages/Contact";
import ProductsPage from "./pages/ProductsPage";
import Products from "./components/Products";

const routes = [
  {
    path: "/",
    element: <App />,
    children: [
      {
        path:"/",
        element: <Home />,
      },
      {
        path: "/products",
        element: <ProductsPage />,
        children: [
          {
            path: "/products/:id",
            element: <Products />
          }
        ]
      },
  
      {
        path: "/about",
        element: <About />,
        
      },
      {
        path: "/contact",
        element: <ContactPage />,
        
      }
    ]
  }
];

export default routes;