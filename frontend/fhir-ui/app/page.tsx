'use client'

import { useState } from 'react'

export default function Home() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<any[]>([])

  const handleSubmit = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      })

      const data = await res.json()
      console.log('FHIR response:', data)

      const condition = data?.conditions?.[0]?.description || 'Unknown'

      // Simulate patient data (since real FHIR data isn't used here)
      const mockResults = [
        { name: 'John Doe', age: 63, condition },
        { name: 'Jane Smith', age: 70, condition }
      ]

      setResults(mockResults)
    } catch (error) {
      console.error('Error fetching FHIR data:', error)
    }
  }

  return (
    <main className="p-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">FHIR Natural Language Query Tool</h1>

      <div className="flex gap-4 mb-6">
        <input
          type="text"
          className="border p-2 flex-1 rounded"
          placeholder="e.g. Show me diabetic patients over 50"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded"
          onClick={handleSubmit}
        >
          Submit
        </button>
      </div>

      {results.length > 0 && (
        <table className="w-full border">
          <thead>
            <tr>
              <th className="border p-2">Name</th>
              <th className="border p-2">Age</th>
              <th className="border p-2">Condition</th>
            </tr>
          </thead>
          <tbody>
            {results.map((patient, index) => (
              <tr key={index}>
                <td className="border p-2">{patient.name}</td>
                <td className="border p-2">{patient.age}</td>
                <td className="border p-2">{patient.condition}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  )
}
