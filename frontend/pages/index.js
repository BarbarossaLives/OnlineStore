import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function Home() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // This would connect to your Saleor GraphQL API
    // For now, we'll use mock data
    const mockProducts = [
      {
        id: 1,
        name: 'Sample Product 1',
        price: 29.99,
        image: 'https://via.placeholder.com/300x300',
        description: 'This is a sample product description.'
      },
      {
        id: 2,
        name: 'Sample Product 2',
        price: 49.99,
        image: 'https://via.placeholder.com/300x300',
        description: 'Another sample product description.'
      }
    ]
    
    setTimeout(() => {
      setProducts(mockProducts)
      setLoading(false)
    }, 1000)
  }, [])

  return (
    <div className="min-h-screen bg-gray-50">
      <Head>
        <title>Your Online Store</title>
        <meta name="description" content="Welcome to our online store powered by Saleor" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className="bg-white shadow-sm">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold text-gray-900">Your Store</h1>
            </div>
            <div className="flex items-center space-x-4">
              <Link href="/cart" className="text-gray-700 hover:text-gray-900">
                Cart (0)
              </Link>
              <Link href="/account" className="text-gray-700 hover:text-gray-900">
                Account
              </Link>
            </div>
          </div>
        </nav>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">Welcome to Our Store</h2>
          
          {loading ? (
            <div className="text-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto"></div>
              <p className="mt-4 text-gray-600">Loading products...</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {products.map((product) => (
                <div key={product.id} className="bg-white rounded-lg shadow-md overflow-hidden">
                  <img 
                    src={product.image} 
                    alt={product.name}
                    className="w-full h-48 object-cover"
                  />
                  <div className="p-4">
                    <h3 className="text-lg font-semibold text-gray-900 mb-2">{product.name}</h3>
                    <p className="text-gray-600 text-sm mb-3">{product.description}</p>
                    <div className="flex justify-between items-center">
                      <span className="text-xl font-bold text-gray-900">${product.price}</span>
                      <button className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors">
                        Add to Cart
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
