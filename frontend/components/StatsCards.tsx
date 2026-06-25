type StatsProps = {
  stats: {
    total: number;
    images: number;
    pdfs: number;
    docx: number;
  };
};

export default function StatsCards({
  stats,
}: StatsProps) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">

      <div className="bg-white rounded-xl shadow p-6 text-center">

        <h3 className="text-gray-500">
          Total Memories
        </h3>

        <p className="text-3xl font-bold mt-2">
          {stats.total}
        </p>

      </div>

      <div className="bg-white rounded-xl shadow p-6 text-center">

        <h3 className="text-gray-500">
          Images
        </h3>

        <p className="text-3xl font-bold mt-2">
          {stats.images}
        </p>

      </div>

      <div className="bg-white rounded-xl shadow p-6 text-center">

        <h3 className="text-gray-500">
          PDFs
        </h3>

        <p className="text-3xl font-bold mt-2">
          {stats.pdfs}
        </p>

      </div>

      <div className="bg-white rounded-xl shadow p-6 text-center">

        <h3 className="text-gray-500">
          DOCX
        </h3>

        <p className="text-3xl font-bold mt-2">
          {stats.docx}
        </p>

      </div>

    </div>
  );
}