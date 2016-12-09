; ModuleID = '../src/test79.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@mem1 = internal global [2 x i32] [i32 291, i32 256], align 4

; Function Attrs: nounwind
define i32 @test79(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  %3 = load i32, i32* getelementptr inbounds ([2 x i32], [2 x i32]* @mem1, i64 0, i64 1), align 4
  %4 = add nsw i32 %2, %3
  store i32 %4, i32* %local, align 4
  %5 = load i32, i32* %local, align 4
  ret i32 %5
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
